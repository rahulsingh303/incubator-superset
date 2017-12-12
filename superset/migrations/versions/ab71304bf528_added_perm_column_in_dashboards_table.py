"""Added perm column in dashboards table

Revision ID: ab71304bf528
Revises: f959a6652acd
Create Date: 2017-11-03 15:09:21.992764

"""

# revision identifiers, used by Alembic.
revision = 'ab71304bf528'
down_revision = 'f959a6652acd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    op.add_column('dashboards', sa.Column('perm', sa.String(length=1000), nullable=True))


def downgrade():
    op.drop_column('dashboards', 'perm')
