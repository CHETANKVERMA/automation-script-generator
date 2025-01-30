document
  .getElementById("steps-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var steps = document.getElementById("steps").value.split(",");

    fetch("/generate_script", {
      // Update URL to match Flask route
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ steps: steps }), // Send the data as JSON
    })
      .then((response) => response.blob())
      .then((blob) => {
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "AutomationScript.java";
        link.click();
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
