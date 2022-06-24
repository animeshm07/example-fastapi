"""add content column to posts table

Revision ID: 7f6fa34a04cc
Revises: 67950d9672cc
Create Date: 2022-06-24 14:16:19.331400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f6fa34a04cc'
down_revision = '67950d9672cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
