package dojo;

import static org.junit.Assert.assertEquals;

import java.util.List;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

public class StepDefinitions {

    private Order order;

    @Given("{word} who wants to buy a drink")
    public void romeo_who_wants_to_buy_a_drink(String from) {
        order = new Order();
        order.declareOwner(from);
    }

    @When("an order is declared for {word}")
    public void an_order_is_declared_for_Juliette(String to) {
        order.declareTarget(to);
    }

    @Then("there is {int} cocktail in the order")
    public void there_is_no_cocktail_in_the_order(Integer int1) {
        List<String> cocktails =  order.getCocktails();
        assertEquals((int)int1, cocktails.size());
    }
}

