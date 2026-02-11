document.getElementById('id_sort').addEventListener('change', function() {
  var selectedValue = this.value;
  // window.location.href = window.location.pathname + '?sort=' + selectedValue;

    var searchParams = new URLSearchParams(window.location.search);
    // console.log(searchParams);
  searchParams.set('sort', selectedValue);
  // console.log(searchParams);
  window.location.href = window.location.pathname + '?' + searchParams.toString();
});
