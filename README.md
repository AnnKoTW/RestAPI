cases.json include all the API information. <br>
    {<br>
		"test_case": "get_count",<br>
		"req_method": "get",<br>
		"req_url": "/api/count",
		"schema":{"type": "object","properties": {"count": {"type": "integer","minimum": 0}},"required": ["count"]},
		"params": {},
		"json": {},
		"test_items":[
		{"scenario": "default", "target": {}, "code_status": 200, "keyword":"count"}
		]
    }
I can check response json schema by "schema"
"target" in "test_items" is the test variable, and "code_status" and "keyword" are the expected result.
