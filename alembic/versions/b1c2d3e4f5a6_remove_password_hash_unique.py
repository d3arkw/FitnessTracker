"""Remove unique constraint from password_hash

Revision ID: b1c2d3e4f5a6
Revises: 8a969f9ca9e7
Create Date: 2026-08-02 17:55:00.000000

"""
from typing import Sequence, Union

from alembic import op


revision: str = 'b1c2d3e4f5a6'
down_revision: Union[str, Sequence[str], None] = '8a969f9ca9e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('users_password_hash_key', 'users', type_='unique')


def downgrade() -> None:
    op.create_unique_constraint('users_password_hash_key', 'users', ['password_hash'])
