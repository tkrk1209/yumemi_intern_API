"""Create table

Revision ID: 6ad16dfd2d1d
Revises: 
Create Date: 2020-06-23 17:09:53.950602+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ad16dfd2d1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_groups_group'), 'groups', ['group'], unique=True)
    op.create_table('ng_words',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ng_word', sa.String(length=50), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ng_word', 'group_id')
    )
    op.create_index('ng_word_and_group_id_idx', 'ng_words', ['ng_word', 'group_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ng_word_and_group_id_idx', table_name='ng_words')
    op.drop_table('ng_words')
    op.drop_index(op.f('ix_groups_group'), table_name='groups')
    op.drop_table('groups')
    # ### end Alembic commands ###