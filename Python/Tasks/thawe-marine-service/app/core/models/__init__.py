import os

from ...common import read_properties_file

sql_scripts = read_properties_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mysql/sql.properties'))

from .mysql import (get_all_eid, insert_many_eid, MysqlDatabaseHandler, get_vessel_id,
                    insert_into_vessel_noon_report,get_noon_report_base_parameter)
