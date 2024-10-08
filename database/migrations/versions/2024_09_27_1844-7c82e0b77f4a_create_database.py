"""create database

Revision ID: 7c82e0b77f4a
Revises: 276db51523d6
Create Date: 2024-09-27 18:44:04.802116

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c82e0b77f4a"
down_revision: Union[str, None] = "276db51523d6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "replacements",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("current_value", sa.String(), nullable=False),
        sa.Column("replace", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("current_value"),
    )
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("url", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("urls")
    op.drop_table("replacements")
    # ### end Alembic commands ###
