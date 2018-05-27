"""empty message

Revision ID: a0835ba30df5
Revises: 
Create Date: 2018-05-29 17:07:01.165938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0835ba30df5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('status', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_signals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('service', sa.Float(), nullable=False),
    sa.Column('shift', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('signals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('type_signal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['type_signal_id'], ['type_signals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ar_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('error', sa.Float(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('signal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['signal_id'], ['signals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('signal_samples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('is_predict', sa.Boolean(), nullable=False),
    sa.Column('signal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['signal_id'], ['signals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ar_model_coeffs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('lag_order', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('ar_model_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ar_model_id'], ['ar_models.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ar_model_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ar_model_coeffs')
    op.drop_table('signal_samples')
    op.drop_table('ar_models')
    op.drop_table('signals')
    op.drop_table('type_signals')
    op.drop_table('devices')
    # ### end Alembic commands ###
