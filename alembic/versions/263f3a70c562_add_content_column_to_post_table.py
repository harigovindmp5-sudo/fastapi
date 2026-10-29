"""add content column to post table

Revision ID: 263f3a70c562
Revises: dbb160199d5c
Create Date: 2026-10-05 15:14:23.935754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '263f3a70c562'
down_revision: Union[str, Sequence[str], None] = 'dbb160199d5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
   op.drop_column('posts','content')
   pass
