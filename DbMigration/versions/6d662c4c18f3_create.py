"""create

Revision ID: 6d662c4c18f3
Revises: 
Create Date: 2022-10-04 14:54:30.956245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d662c4c18f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('register',sa.Column('id',sa.Integer(),nullable = False,primary_key = True))


def downgrade() -> None:
    pass
