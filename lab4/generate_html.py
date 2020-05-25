import pandas as pd 

url = 'https://gist.githubusercontent.com/bshmueli/c99fc0abf56460e644bd610bf3024e83/raw/720285d133c85d94e0aa3fe3edcc199f6d99e3f7/lab4-data.csv'
corpus_df = pd.read_csv(url)

corpus = corpus_df.values[:, 1]
idx = corpus_df.values[:, 0]

for i in range(len(corpus)):
    html = f'''<!doctype html>
<html lang="en">
<head>
	<meta content="text/html;charset=UTF-8" http-equiv="Content-Type" />
	<script src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js' type='text/javascript'></script>

</head>
<body>
	<form id="mturk_form" method="post" name="mturk_form">
		<input type="hidden" id="assignmentId" value="" name="assignmentId"/>
		<input type="hidden" id="CorpusIdx" value="{idx[i]}" name="CorpusIdx"/>

        <fieldset>
            <h1>
                {corpus[i]}
            </h1>
        </fieldset>
        <br>

		<h2>Choose one emotion that most matches the text in each block.</h2>

		<fieldset>
			<p><label><input name="valence" type="radio" value="Pleasant" /> Pleasant</label></p>
			<p><label><input name="valence" type="radio" value="Pleased" /> Pleased</label></p>
			<p><label><input name="valence" type="radio" value="Neutral" /> Neutral</label></p>
			<p><label><input name="valence" type="radio" value="Unsatisfied" />  Unsatisfied</label></p>
			<p><label><input name="valence" type="radio" value="Unpleasant" />  Unpleasant</label></p>
		</fieldset>
		<br>

		<fieldset>
			<p><label><input name="arousal" type="radio" value="Excited" /> Excited</label></p>
			<p><label><input name="arousal" type="radio" value="Wide-awake" /> Wide-awake</label></p>
			<p><label><input name="arousal" type="radio" value="Neutral" /> Neutral</label></p>
			<p><label><input name="arousal" type="radio" value="Dull" />  Dull</label></p>
			<p><label><input name="arousal" type="radio" value="Calm" />  Calm</label></p>
		</fieldset>
		<br>

		<fieldset>
			<p><label><input name="dominance" type="radio" value="Dependent" /> Dependent</label></p>
			<p><label><input name="dominance" type="radio" value="Powerlessness" /> Powerlessness</label></p>
			<p><label><input name="dominance" type="radio" value="Neutral" /> Neutral</label></p>
			<p><label><input name="dominance" type="radio" value="Powerful" />  Powerful</label></p>
			<p><label><input name="dominance" type="radio" value="Independent" />  Independent</label></p>
		</fieldset>
		<br>
		<input type="submit">
	</form>
	<script language='Javascript'>turkSetAssignmentID();</script>
</body>
</html>'''

    file_ = open(f'./html/{idx[i]}.html', 'w')
    file_.write(html)
    file_.close()

    print(f'Saved {idx[i]}.html', end='\r', flush=True)
    