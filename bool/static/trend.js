const url = "http://localhost:5000/bool/api/best";
console.log(url)
fetch(url)
    .then((response) => response.json())
    .then((data) => {
        const trendPanels = document.querySelectorAll(".trendList .trendPanel");

        for (let i = 0; i < data.length; i++) {
            const title = data[i].subject;
            const content = data[i].content;

            const titleElement = trendPanels[i].querySelector(".trendPanelTitle");
            const contentElement = trendPanels[i].querySelector(
                ".trendPanelContent"
            );

            titleElement.textContent = title;
            titleElement.setAttribute('href', `http://localhost:5000/bool/detail/${data[i].id}`)
            contentElement.textContent = content;
        }
    });

const reloadButton = document.querySelector(".reloadTrends");

reloadButton.addEventListener("click", () => {
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            const trendPanels = document.querySelectorAll(".trendList .trendPanel");

            for (let i = 0; i < data.length; i++) {
                const title = data[i].subject;
                const content = data[i].content;

                const titleElement = trendPanels[i].querySelector(".trendPanelTitle");
                const contentElement = trendPanels[i].querySelector(
                    ".trendPanelContent"
                );

                titleElement.textContent = title;
                contentElement.textContent = content;
            }
        });
});
