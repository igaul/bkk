const spinnerEl = document.getElementById("spinner");
spinnerEl.style.display = "none";
const searchFormEl = document.getElementById("searchform");
const resultsEl = document.getElementById("results");

function search(query, filter) {
  spinnerEl.style.display = "block";
  const url =
    "https://bkk.schepman.org/jsonp?search=" +
    encodeURIComponent(query) +
    "&searchby=" +
    encodeURIComponent(filter) +
    "&jsoncallback=?";
  console.log({ url });
  fetch(url)
    .then(response => response.json())
    .then(data => {
      let table = "<table><tr><th>Artist</th><th>Title</th></tr>";
      data.forEach(function (item) {
        table +=
          "<tr><td>" + item.artist + "</td><td>" + item.title + "</td></tr>";
      });
      spinnerEl.style.display = "none";
      resultsEl.innerHTML = table;
    })
    .catch(error => console.log(error))
    .finally(() => (spinnerEl.style.display = "none"));
}

searchFormEl.addEventListener("submit", function (event) {
  event.preventDefault();
  const searchEl = document.getElementById("search");
  const searchbyEl = document.getElementById("searchby");
  const search = searchEl.value;
  const searchby = searchbyEl.value;
  if (search !== "") {
    search(search, searchby);
  }
});
