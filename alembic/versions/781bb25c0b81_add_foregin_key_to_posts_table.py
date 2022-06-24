"""add foregin-key to posts table

Revision ID: 781bb25c0b81
Revises: 0b623a8f7d34
Create Date: 2022-06-24 14:34:50.834827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '781bb25c0b81'
down_revision = '0b623a8f7d34'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')

    
