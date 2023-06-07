const recommend_elements = document.getElementsByClassName("recommend");
const notRecommend_elements = document.getElementsByClassName("notRecommend");
Array.from(recommend_elements).forEach(function (element) {
    element.addEventListener('click', function () {
        if (confirm("정말로 추천하시겠습니까?")) {
            location.href = this.dataset.uri;
        }
        ;
    });
});
Array.from(notRecommend_elements).forEach(function (element) {
    element.addEventListener('click', function () {
        if (confirm("정말로 비추천하시겠습니까?")) {
            location.href = this.dataset.uri;
        }
        ;
    });
});

console.log(recommend_elements)
console.log(notRecommend_elements)