"""empty message

Revision ID: dfad1f2acb22
Revises: 3420f22521af
Create Date: 2016-07-22 20:42:29.013839

"""

# revision identifiers, used by Alembic.
revision = 'dfad1f2acb22'
down_revision = '3420f22521af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notify', sa.Column('append_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notify', 'append_id')
    ### end Alembic commands ###
