"""empty message

Revision ID: 3bb84c3c0f77
Revises: 3fbe17b98982
Create Date: 2022-10-29 15:05:11.428495

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3bb84c3c0f77'
down_revision = '3fbe17b98982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('People',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=256), nullable=True),
    sa.Column('skin_color', sa.String(length=256), nullable=True),
    sa.Column('eye_color', sa.String(length=256), nullable=True),
    sa.Column('birth_year', sa.String(length=256), nullable=True),
    sa.Column('gender', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.drop_index('id', table_name='people')
    op.drop_index('id_2', table_name='people')
    op.drop_table('people')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('height', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mass', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hair_color', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('skin_color', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('eye_color', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('birth_year', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id_2', 'people', ['id'], unique=False)
    op.create_index('id', 'people', ['id'], unique=False)
    op.drop_table('People')
    # ### end Alembic commands ###
