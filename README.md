cases.json include all the API information. <br>
    {<br>
		"test_case": "get_count",<br>
		"req_method": "get",<br>
		"req_url": "/api/count",<br>
		"schema":{"type": "object","properties": {"count": {"type": "integer","minimum": 0}},"required": ["count"]},<br>
		"params": {},<br>
		"json": {},<br>
		"test_items":[<br>
		{"scenario": "default", "target": {}, "code_status": 200, "keyword":"count"}<br>
		]<br>
    }<br>
I can check response json schema by "schema"<br>
"target" in "test_items" is the test variable, and "code_status" and "keyword" are the expected result.<br>
