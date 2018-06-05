'using sctrict';

Chart.defaults.global.defaultFontFamily = "arial";

Chart.defaults.global.defaultFontSize = 15;

function createNumberArray(start, count, step=1) {
    var a = [];
    for (var i = start; i <= start + count; i+=step) {
        a.push(i);
    }
    return a;
}


var endogenDataSet = {
    data: [],
    label: 'Входные значения',
    borderColor: 'blue',
    borderWidth: 1
};
var predictDataSet = {
    data: [],
    label: 'Предсказанные',
    borderColor: 'green',
    borderWidth: 1,
    backgroundColor: 'transparent'
};
var chartOptions = {
    scales: {
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Уровень сигнала'
            },
            ticks: {beginAtZero:false}
        }],
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Такты времени'
            },
            ticks: {maxTicksLimit: 20}
        }]
    },
    annotation: {
        drawTime: 'afterDatasetsDraw',
        events: ['click'],
        dblClickSpeed: 350,
        annotations: [{
            drawTime: 'afterDraw', // overrides annotation.drawTime if set
            id: 'a-line-0', // optional
            type: 'line',
            mode: 'horizontal',
            scaleID: 'y-axis-0',
            value: 0,
            borderColor: 'yellow',
            borderWidth: 2,
            label: {
                content: 'Тех. Обсл.',
                enabled: true,
                position: 'left'
            },
        },{
            drawTime: 'afterDraw', // overrides annotation.drawTime if set
            id: 'a-line-1', // optional
            type: 'line',
            mode: 'horizontal',
            scaleID: 'y-axis-0',
            value: 0,
            borderColor: 'red',
            borderWidth: 2,
            label: {
                content: 'Замена',
                enabled: true,
                position: 'left'
            },
        }]
    },
    responsive: true,
    maintainAspectRatio: false
};



/*
 * Vue Chart Component
 */
Vue.component('line-chart',
{
    extends: VueChartJs.Line,

    mounted: function () {
        this.renderChart({
            labels: createNumberArray(0, 60),
            datasets: [endogenDataSet, predictDataSet]
        }, chartOptions);
    }
});

/*
 * Async Requests
 */
function query(url, postData = null) {
    var promise = new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open(postData !== null ? 'POST' : 'GET', url);
        xhr.onload = () => {
            var data = null;
            try { resolve(JSON.parse(xhr.responseText)); }
            catch (e) { reject(e); }
        }
        xhr.send();
    });
    promise.catch(alert.bind(this,
        'Не могу получить данные. Проверьте соединение с сервером'
    ));
    return promise;
}

/*
 * Vue Application
 */
var app = new Vue({
    el: '#app',
    data: {
        status: 'ready',
        selSignal: null,
        selDevice: null,
        devices: null,
        showPopup: false,
    },
    computed: {
        isReady: function() {
            return this.devices !== null;
        }
    },
    methods: {
        getDevices: function() {
            query('/api/devices').then((data) => {
                this.devices = data;
            });
        },
        canRecalcDevice: function(device) {
            return (device.actual_signals || []).every(s => s.primary_ar_model);
        },
        recalcDevice: function(device) {
            this.devices = null;
            query(`/api/device/${device.id}/analyze`).then(this.getDevices);
        },
        getLastSignalSample: function(signal) {
            if (signal.endog_samples.length > 0)
                return signal.endog_samples.slice(-1)[0]

            return '–';
        },
        getSignalService: function(signal) {
            var ar_model = signal.primary_ar_model;
            if (ar_model !== null)
                return ar_model.steps_before_service;

            return '–';
        },
        getSignalShift: function(signal) {
            var ar_model = signal.primary_ar_model;
            if (ar_model !== null)
                return ar_model.steps_before_shift;

            return '–';
        },
        showSignal: function(device, signal) {
            // view actions
            this.selDevice = device;
            this.selSignal = signal;
            this.showPopup = true;

            var endogs = signal.endog_samples.slice(-30);
            endogenDataSet.data = endogs;
            predictDataSet.data = endogs.concat(signal.predict_samples);

            //preset annotations
            var a = chartOptions.annotation.annotations;
            a[0].value = signal.type_signal.service;
            a[1].value = signal.type_signal.shift;
        },
        hidePopup: function(e) {
            this.showPopup = !e.target.classList.contains('closeOnClk');
        },
        momentWr: function(time) {
            return moment(new Date(time)).calendar();
        },
        resolveStatusClassName: function(status) {
            if (status < 50)
                return 'red darken-'+(Math.ceil(status / 12.5));
            else
                return 'green darken-'+(4-Math.ceil((status - 50) / 12.5));
        },
    },
    mounted: function() {
        this.getDevices();
    },
    rendered: function() {
        M.AutoInit();
    }
});

