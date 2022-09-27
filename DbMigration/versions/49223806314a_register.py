"""register

Revision ID: 49223806314a
Revises: 
Create Date: 2022-09-27 12:27:39.726834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49223806314a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('register',sa.Column('id',sa.Integer(),nullable = False,primary_key=True))



def downgrade() -> None:
    op.drop_column("register","id")
