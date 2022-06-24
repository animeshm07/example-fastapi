"""create users table

Revision ID: 0b623a8f7d34
Revises: 7f6fa34a04cc
Create Date: 2022-06-24 14:21:26.909962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b623a8f7d34'
down_revision = '7f6fa34a04cc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'), nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('users')
