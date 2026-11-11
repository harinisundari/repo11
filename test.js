
const { Builder, By } = require("selenium-webdriver");

function test_addition() {
    const driver = new Builder().forBrowser("chrome").build();

    driver.then(async (browser) => {
        try {
            await browser.get("http://localhost:8000/calculator.html");

            await browser.findElement(By.id("num1")).sendKeys("10");
            await browser.findElement(By.id("num2")).sendKeys("20");
            await browser.findElement(By.id("addBtn")).click();

            const result = await browser.findElement(By.id("result")).getText();

            console.log("Result:", result);

            if (result === "30") {
                console.log("TEST PASSED");
            } else {
                console.log("TEST FAILED");
            }
        } finally {
            await browser.quit();
        }
    });
}

test_addition();
