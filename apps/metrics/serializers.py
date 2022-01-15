from rest_framework import serializers

from .models import Metrics


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('group_by')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MetricsSerializer(DynamicFieldsModelSerializer):
    cpi = serializers.SerializerMethodField()

    def get_cpi(self, obj):
        return obj.cpi

    class Meta:
        model = Metrics
        fields = '__all__'
