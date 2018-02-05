"""create live network umts cells data view

Revision ID: cfc100311d9f
Revises: 1faf6c2610bb
Create Date: 2018-02-05 14:08:06.239000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfc100311d9f'
down_revision = '1faf6c2610bb'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_umts_cells_data AS
     SELECT t1.name,
        t2.name AS site,
        t4.name AS node,
        t3.name AS vendor,
        t1.bch_power,
        t1.cell_id AS ci,
        t1.lac,
        t1.latitude,
        t1.longitude,
        t1.maximum_transmission_power AS maxtx_power,
        t1.primary_sch_power,
        t1.rac,
        t1.sac,
        t1.secondary_sch_power,
        t1.uarfcn_dl,
        t1.uarfcn_ul,
        t1.ura_list,
        t1.azimuth,
        t1.cpich_power,
        t1.scrambling_code,
        t1.cell_range,
        t1.height,
        t1.site_sector_carrier
       FROM live_network.umts_cells_data t1
         JOIN live_network.sites t2 ON t2.pk = t1.pk
         JOIN vendors t3 ON t3.pk = t1.vendor_pk
         JOIN live_network.nodes t4 ON t4.pk = t2.node_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_umts_cells_data""")