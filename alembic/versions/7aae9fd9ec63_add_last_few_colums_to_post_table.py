"""add last few colums to post table

Revision ID: 7aae9fd9ec63
Revises: d1d7b1f49faf
Create Date: 2026-10-25 19:45:13.215344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7aae9fd9ec63'
down_revision: Union[str, Sequence[str], None] = 'd1d7b1f49faf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass
    
   



def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posys','created_at')
    pass
    
    
