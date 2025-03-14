from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(instance, "added_at"):
            data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M:%S")
        if hasattr(instance, "updated_at"):
            data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        return data


def build_relational_model_serializer(model_, fields_=None, exclude_=None, ref_name_=None):
    class RelationalSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_
            if fields_ is not None:
                fields = fields_
            else:
                exclude = exclude_
            ref_name = ref_name_

    return RelationalSerializer()

