"""zabbix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from zabbix.initializer import initialize_zabbix
from django.conf import urls
from .views import HostGroupObject,\
                    HostGroupRename,\
                    HostObjects,\
                    HostObject,\
                    HostTemplates,\
                    HostInterfaces,\
                    HostStandardSnmp,\
                    HostAlarms,\
                    CheckForHostsExistence,\
                    Items,\
                    HistoricData
from django.conf.urls import url
from MonitoringIntegration.settings import sync_with_db
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MobileNoc Zabbix API')


urlpatterns = [

    # PROD section
    # Host Endpoints
    urls.url(r'zabbix/hosts/', HostObjects.as_view({'get': 'get_enabled_hosts'})),
    urls.url(r'^zabbix/hostdetail/(?P<machine_id>.+)/$', HostObject.as_view({'get': 'get_host'})),

    # To add host manually
    urls.url(r'zabbix/hostsaddsnmp/', HostStandardSnmp.as_view({'post': 'add_host'})),

    # historical data
    urls.url(r'^zabbix/historical/cpu/(?P<machine_id>.+)/$', HistoricData.as_view({'get': 'cpu_data'})),
    urls.url(r'^zabbix/historical/ram_free/(?P<machine_id>.+)/$', HistoricData.as_view({'get': 'free_ram_data'})),
    urls.url(r'^zabbix/historical/ram_used/(?P<machine_id>.+)/$', HistoricData.as_view({'get': 'used_ram_data'})),

    # list Alarms for a host
    urls.url(r'^zabbix/alarms/(?P<machine_id>.+)/$', HostAlarms.as_view({'get': 'list_host_alarms'})),

    # NON-PROD section
    # parameter checking for internal use
    urls.url(r'^zabbix-non-prod/non-prod/templates/(?P<machine_id>.+)/$', HostTemplates.as_view({'get': 'get_templates'})),
    urls.url(r'^zabbix-non-prod/non-prod/items/(?P<keyname>.+)/$', Items.as_view({'get': 'get_items'})),

    # HostGroup Endpoints

    # urls.url(r'zabbix/checkhostsexistence/', CheckForHostsExistence.as_view({'put': 'by_host_name'})),
    # urls.url(r'zabbix/hostgroups/', HostGroupObject.as_view({'put': 'list_groups'})),
    # urls.url(r'zabbix/hostgroupcreate/', HostGroupObject.as_view({'put': 'add_group'})),
    # urls.url(r'zabbix/hostgroupdetail/', HostGroupObject.as_view({'put': 'get_group'})),
    # urls.url(r'zabbix/hostgroupdelete/', HostGroupObject.as_view({'put': 'delete_group'})),
    # urls.url(r'zabbix/hostgrouprename/', HostGroupRename.as_view({'put': 'rename_group'})),

    # templ
    # Interfaces added to host
    # urls.url(r'zabbix/hostinterfaces/', HostInterfaces.as_view({'put': 'get_interfaces'})),


    # Swagger Schema
    url(r'^$', schema_view)
               ]
print (sync_with_db)
if sync_with_db is True:
    initialize_zabbix()

