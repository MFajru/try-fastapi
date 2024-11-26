"""add created_at updated_at

Revision ID: 7d6cd115eb97
Revises: 51b5ae4ff5c5
Create Date: 2024-11-26 16:43:23.539693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d6cd115eb97'
down_revision: Union[str, None] = '51b5ae4ff5c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('author', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.add_column('book', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('book', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'updated_at')
    op.drop_column('book', 'created_at')
    op.drop_column('author', 'updated_at')
    op.drop_column('author', 'created_at')
    # ### end Alembic commands ###
