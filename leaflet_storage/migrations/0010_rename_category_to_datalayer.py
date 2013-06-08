# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming model 'Category' to 'DataLayer'
        db.rename_table(u'leaflet_storage_category', u'leaflet_storage_datalayer')
        db.send_create_signal(u'leaflet_storage', ['DataLayer'])

        # Renaming fields '.category_id' to '.datalayer_id'
        db.rename_column(u'leaflet_storage_polyline', 'category_id', 'datalayer_id')
        db.rename_column(u'leaflet_storage_polygon', 'category_id', 'datalayer_id')
        db.rename_column(u'leaflet_storage_marker', 'category_id', 'datalayer_id')

    def backwards(self, orm):
        # Renaming model 'Category' to 'DataLayer'
        db.rename_table(u'leaflet_storage_datalayer', u'leaflet_storage_category')
        db.send_create_signal(u'leaflet_storage', ['Category'])

        # Renaming fields '.category_id' to '.datalayer_id'
        db.rename_column(u'leaflet_storage_polyline', 'datalayer_id', 'category_id')
        db.rename_column(u'leaflet_storage_polygon', 'datalayer_id', 'category_id')
        db.rename_column(u'leaflet_storage_marker', 'datalayer_id', 'category_id')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'leaflet_storage.datalayer': {
            'Meta': {'ordering': "('name',)", 'object_name': 'DataLayer'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_on_load': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.Map']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('leaflet_storage.fields.DictField', [], {'null': 'True', 'blank': 'True'}),
            'pictogram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.Pictogram']", 'null': 'True', 'blank': 'True'})
        },
        u'leaflet_storage.licence': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Licence'},
            'details': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'leaflet_storage.map': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Map'},
            'center': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edit_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '3'}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.Licence']", 'on_delete': 'models.SET_DEFAULT'}),
            'locate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_maps'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'settings': ('leaflet_storage.fields.DictField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tilelayers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leaflet_storage.TileLayer']", 'through': u"orm['leaflet_storage.MapToTileLayer']", 'symmetrical': 'False'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {'default': '7'})
        },
        u'leaflet_storage.maptotilelayer': {
            'Meta': {'ordering': "['rank', 'tilelayer__name']", 'object_name': 'MapToTileLayer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.Map']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tilelayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.TileLayer']"})
        },
        u'leaflet_storage.marker': {
            'Meta': {'object_name': 'Marker'},
            'datalayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.DataLayer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('leaflet_storage.fields.DictField', [], {'null': 'True', 'blank': 'True'}),
            'pictogram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.Pictogram']", 'null': 'True', 'blank': 'True'})
        },
        u'leaflet_storage.pictogram': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Pictogram'},
            'attribution': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pictogram': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'leaflet_storage.polygon': {
            'Meta': {'object_name': 'Polygon'},
            'datalayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.DataLayer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.contrib.gis.db.models.fields.PolygonField', [], {'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('leaflet_storage.fields.DictField', [], {'null': 'True', 'blank': 'True'})
        },
        u'leaflet_storage.polyline': {
            'Meta': {'object_name': 'Polyline'},
            'datalayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['leaflet_storage.DataLayer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.contrib.gis.db.models.fields.LineStringField', [], {'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('leaflet_storage.fields.DictField', [], {'null': 'True', 'blank': 'True'})
        },
        u'leaflet_storage.tilelayer': {
            'Meta': {'ordering': "('rank', 'name')", 'object_name': 'TileLayer'},
            'attribution': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxZoom': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'minZoom': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rank': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url_template': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['leaflet_storage']
