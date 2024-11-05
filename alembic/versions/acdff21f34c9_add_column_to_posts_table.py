"""add column to posts table

Revision ID: acdff21f34c9
Revises: 1c5db8258060
Create Date: 2024-11-05 04:17:44.568779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acdff21f34c9'
down_revision: Union[str, None] = '1c5db8258060'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass