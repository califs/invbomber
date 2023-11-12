from django.db import models


class Articulos(models.Model):
    id_articulo = models.IntegerField(db_column='ID_ARTICULO', primary_key=True)  # Field name made lowercase.
    id_bodega = models.ForeignKey('BodegaCentral', models.DO_NOTHING, db_column='ID_BODEGA', blank=True, null=True)  # Field name made lowercase.
    codigo_art = models.CharField(db_column='CODIGO_ART', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_art = models.CharField(db_column='NOMBRE_ART', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marca_art = models.CharField(db_column='MARCA_ART', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descrip_art = models.CharField(db_column='DESCRIP_ART', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidad_art = models.IntegerField(db_column='CANTIDAD_ART', blank=True, null=True)  # Field name made lowercase.
    tipo_art = models.CharField(db_column='TIPO_ART', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ano_adquisicion = models.CharField(db_column='ANO_ADQUISICION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vida_util = models.CharField(db_column='VIDA_UTIL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    estado_art = models.CharField(db_column='ESTADO_ART', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imagen = models.ImageField(db_column='IMAGEN',  verbose_name="imagen", null=True)
    class Meta:
        managed = False
        db_table = 'articulos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BodegaCentral(models.Model):
    id_bodega = models.IntegerField(db_column='ID_BODEGA', primary_key=True)  # Field name made lowercase.
    encargado_alm = models.CharField(db_column='ENCARGADO_ALM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion_alm = models.CharField(db_column='DIRECCION_ALM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono_alm = models.CharField(db_column='TELEFONO_ALM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comuna_alm = models.CharField(db_column='COMUNA_ALM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email_alm = models.CharField(db_column='EMAIL_ALM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bodega_central'


class BomberosArticulos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bomberos_articulos'


class Distribucion(models.Model):
    id_distribucion = models.IntegerField(db_column='ID_DISTRIBUCION', primary_key=True)  # Field name made lowercase.
    id_bodega = models.ForeignKey(BodegaCentral, models.DO_NOTHING, db_column='ID_BODEGA', blank=True, null=True)  # Field name made lowercase.
    cant_veh = models.IntegerField(db_column='CANT_VEH', blank=True, null=True)  # Field name made lowercase.
    cant_art = models.IntegerField(db_column='CANT_ART', blank=True, null=True)  # Field name made lowercase.
    nom_pers = models.CharField(db_column='NOM_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distribucion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InvVeh(models.Model):
    id_inv_veh = models.IntegerField(db_column='ID_INV_VEH', primary_key=True)  # Field name made lowercase.
    id_veh = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='ID_VEH', blank=True, null=True)  # Field name made lowercase.
    codigo_inv_veh = models.CharField(db_column='CODIGO_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    patente_inv_veh = models.CharField(db_column='PATENTE_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_inv_veh = models.CharField(db_column='NOMBRE_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidad_inv_veh = models.IntegerField(db_column='CANTIDAD_INV_VEH', blank=True, null=True)  # Field name made lowercase.
    seccion_inv_veh = models.CharField(db_column='SECCION_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado_inv_veh = models.CharField(db_column='ESTADO_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    responsable_inv_veh = models.CharField(db_column='RESPONSABLE_INV_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inv_veh'


class Personal(models.Model):
    id_personal = models.IntegerField(db_column='ID_PERSONAL', primary_key=True)  # Field name made lowercase.
    id_bodega = models.ForeignKey(BodegaCentral, models.DO_NOTHING, db_column='ID_BODEGA', blank=True, null=True)  # Field name made lowercase.
    rut_pers = models.CharField(db_column='RUT_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_pers = models.CharField(db_column='NOMBRE_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido_pers = models.CharField(db_column='APELLIDO_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechanac_pers = models.CharField(db_column='FECHANAC_PERS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    edad_pers = models.CharField(db_column='EDAD_PERS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono_pers = models.CharField(db_column='TELEFONO_PERS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    correo_pers = models.CharField(db_column='CORREO_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion_pers = models.CharField(db_column='DIRECCION_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comuna_pers = models.CharField(db_column='COMUNA_PERS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal'


class TipoUsuario(models.Model):
    id_usu = models.IntegerField(db_column='ID_USU', primary_key=True)  # Field name made lowercase.
    id_bodega = models.ForeignKey(BodegaCentral, models.DO_NOTHING, db_column='ID_BODEGA', blank=True, null=True)  # Field name made lowercase.
    id_personal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='ID_PERSONAL', blank=True, null=True)  # Field name made lowercase.
    nom_usu = models.CharField(db_column='NOM_USU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grado_usu = models.CharField(db_column='GRADO_USU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado_usu = models.CharField(db_column='ESTADO_USU', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Vehiculo(models.Model):
    id_veh = models.IntegerField(db_column='ID_VEH', primary_key=True)  # Field name made lowercase.
    id_bodega = models.ForeignKey(BodegaCentral, models.DO_NOTHING, db_column='ID_BODEGA', blank=True, null=True)  # Field name made lowercase.
    marca_veh = models.CharField(db_column='MARCA_VEH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    patente_veh = models.CharField(db_column='PATENTE_VEH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipo_veh = models.CharField(db_column='TIPO_VEH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descrip_veh = models.CharField(db_column='DESCRIP_VEH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    anoingreso_veh = models.CharField(db_column='ANOINGRESO_VEH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ultima_mantencion = models.CharField(db_column='ULTIMA_MANTENCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    proxima_mantencion = models.CharField(db_column='PROXIMA_MANTENCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estado_veh = models.CharField(db_column='ESTADO_VEH', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehiculo'
