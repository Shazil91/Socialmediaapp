"""add content column to posts table

Revision ID: 3f175e5db992
Revises: da49d06357dd
Create Date: 2024-10-27 23:16:53.715620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f175e5db992'
down_revision: Union[str, None] = 'da49d06357dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
