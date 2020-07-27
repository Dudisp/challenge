import json


class Validator:
    @staticmethod
    def validate_line_as_json(json_line):
        try:
            json_object = json.loads(json_line)
        except Exception as e:
            print(f"line was not a valid json: {json_line}")  # in case json is invalid
            return None
        else:
            return json_object
