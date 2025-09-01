"""add messages

Revision ID: a608284e3773
Revises: 8a1f23ff23ee
Create Date: 2025-08-27 16:20:38.063482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a608284e3773'
down_revision: Union[str, Sequence[str], None] = '8a1f23ff23ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('messages',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('chat_id', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('messages')
    # ### end Alembic commands ###
