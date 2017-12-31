
$(document).ready(function(){

  function perc(a, b) {
    var math = b.amt / a;
    return math;
  };

  var T_form = function(a, b, c)
  {
      this.name = a;
      this.amt = b;
      this.plus_minus = c;
  };

  function transact(a, b) {
    if (b.plus_minus == "expense") {
      balance = a - b.amt;
  };
  };


  var balance = inc;
    var t_list = [];

  $(".form").submit(function() {
      var name = $("#name").val();
      var amt = $("#amt").val();
      var plus_minus = $(".form input[type='radio']:checked").val();

      var tra = new T_form(name, amt, plus_minus);

      transact(balance, tra);

      t_list.push(tra);

      $(".main").append("<h3>Tranaction Name: " + name +  "Transaction percentage: " + perc(inc, tra) + "</h3>");

      event.preventDefault();
  });
});
