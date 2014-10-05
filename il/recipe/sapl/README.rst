Supported options
=================

The recipe supports the following options:

sapl-id
    The id of the SAPL that the script will create.
    Default: sapl

admin-user
    The id of an admin user that will be used as the ``Manager``.
    Default: ``admin``

container-path
    The path (relative from Zope root) to the container that should hold sapl_documentos.
    It's important to inform the full path, including the SAPL container.
    Default: ``/sapl/sapl_documentos``

mysql-user
    The user of an admin user that will be used to create the database, tables and SAPL MySQL user.
    Default: ``root``

mysql-pass
    The password of mysql-user.
    Default: ``root``

mysql-host
    The mysql host
    Default: ``localhost``

mysql-db
    The mysql database name that will be created. If database name is different
    than the default name, it's necessary to change it in the MySQL connector.
    Default: ``interlet``

add-mountpoint
    Adds the ZODB Mount Point at the path specified by ``container-path``
