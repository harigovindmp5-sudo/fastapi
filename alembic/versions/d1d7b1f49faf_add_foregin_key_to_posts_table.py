"""add foregin-key to posts table

Revision ID: d1d7b1f49faf
Revises: 460252a1fcad
Create Date: 2026-10-24 20:21:42.981159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1d7b1f49faf'
down_revision: Union[str, Sequence[str], None] = '460252a1fcad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )

    op.create_foreign_key(
        'post_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
