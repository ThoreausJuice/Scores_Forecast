<?php
	set_time_limit(0);
	ini_set("memory_limit", "-1");
	ini_set("max_execution_time", "0");
	if (isset($_GET["studentid"]) && isset($_GET["coursetype"]) &&
		isset($_GET["coursescore"]) && isset($_GET["examtype"]))
	{
		$execCommand = "python3 Predict_Application.py " . $_GET["studentid"] . " " . $_GET["coursetype"] . " " . $_GET["coursescore"] . " " . $_GET["examtype"];
		fwrite(fopen("1.txt", 'w'), $_GET["studentid"] . "," . $_GET["coursetype"] . "," . $_GET["coursescore"] . "," . $_GET["examtype"]);
		passthru("python3 Predict_Application.py", $returnVal);
		$result = file_get_contents("2.txt");
		print($result);
	}
	else
	{
		print("Invalid Arguments.");
	}
?>
