<!-- src/Sentiment.svelte -->
<script>
  let text = "";
  let scores = {
    positive: 0,
    negative: 0,
    neutral: 0,
    compound: 0,
  };

  async function analyzeSentiment() {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/sentiment/q?=${encodeURIComponent(text)}`
      );
      const data = await response.json();
      scores = data;
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<div class="container">
  <input type="text" bind:value={text} placeholder="Enter a sentence..." />
  <button on:click={analyzeSentiment}>Analyze</button>
</div>

<div class="scores">
  <div class="score-label positive">Positive:</div>
  <div class="score-bar positive" style={`width: ${scores.positive * 100}%`} />

  <div class="score-label negative">Negative:</div>
  <div class="score-bar negative" style={`width: ${scores.negative * 100}%`} />

  <div class="score-label neutral">Neutral:</div>
  <div class="score-bar neutral" style={`width: ${scores.neutral * 100}%`} />
</div>

<div class="compound-score">
  <p>Compound Score: {scores.compound}</p>
</div>

<style>
  body {
    background-color: #f0f0f0; /* Background color for the entire webpage */
    font-size: 1.2rem; /* Increase font size */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh; /* Center content vertically */
  }

  .container {
    text-align: center;
    margin: 20px;
  }

  input {
    width: 80%;
    padding: 10px;
  }

  .scores {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 20px;
  }

  .score-label {
    font-weight: bold;
  }

  .score-bar {
    height: 20px; /* Bar height */
    background-color: #469901eb; /* Positive: Green */
    margin-bottom: 5px; /* Add space between progress bars */
  }

  .score-bar.negative {
    background-color: #dc3545; /* Negative: Red */
  }

  .score-bar.neutral {
    background-color: #3586cd; /* Neutral: Blue/Brown */
  }

  .compound-score {
    margin-top: 20px;
  }
</style>
