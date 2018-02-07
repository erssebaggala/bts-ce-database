"""Create vendor cm file format map

Revision ID: 32b1c6af83f6
Revises: 96eb4729fc6d
Create Date: 2018-02-07 15:16:53.155000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b1c6af83f6'
down_revision = '96eb4729fc6d'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'vendors_cm_file_format_map',
        sa.Column('pk', sa.Integer, primary_key=True,  nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('format_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now())
    )
    op.execute('ALTER SEQUENCE  vendors_cm_file_format_map_pk_seq RENAME TO seq_vendors_cm_file_format_map_pk')

    vendors = sa.sql.table(
        'vendors_cm_file_format_map',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_vendors_cm_file_format_map_pk', ), primary_key=True, nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('format_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now())
    )

    op.bulk_insert(vendors, [
        # Ericsson 2G
        {'vendor_pk': '1', 'format_pk': 1, 'tech_pk':'1', 'modified_by': 0, 'added_by': 0},

        # Ericsson 3G
        {'vendor_pk': '1', 'format_pk': 2, 'tech_pk':'2', 'modified_by': 0, 'added_by': 0},

        # Ericsson 3G
        {'vendor_pk': '1', 'format_pk': 3, 'tech_pk':'3', 'modified_by': 0, 'added_by': 0},
        
        # Huawei 2G
        {'vendor_pk': '2', 'format_pk': 4, 'tech_pk':'1', 'modified_by': 0, 'added_by': 0},

        # Huawei 3G
        {'vendor_pk': '2', 'format_pk': 5, 'tech_pk':'2', 'modified_by': 0, 'added_by': 0},

        # Huawei 3G
        {'vendor_pk': '2', 'format_pk': 6, 'tech_pk':'3', 'modified_by': 0, 'added_by': 0},

        # ZTE 2G
        {'vendor_pk': '3', 'format_pk': 7, 'tech_pk': '1', 'modified_by': 0, 'added_by': 0},

        # ZTE 3G
        {'vendor_pk': '3', 'format_pk': 8, 'tech_pk': '2', 'modified_by': 0, 'added_by': 0},

        # ZTE 4G
        {'vendor_pk': '3', 'format_pk': 9, 'tech_pk': '3', 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.drop_table('vendors_cm_file_format_map')