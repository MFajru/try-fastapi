"""update model relation

Revision ID: c636a37d03b3
Revises: b3c1868cc99f
Create Date: 2024-12-02 10:38:51.245122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c636a37d03b3'
down_revision: Union[str, None] = 'b3c1868cc99f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
