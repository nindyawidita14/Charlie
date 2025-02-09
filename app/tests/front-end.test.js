const puppeteer = require('puppeteer');

describe('Dashboard Page Tests', () => {
    let browser;
    let page;

    beforeAll(async () => {
        browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        page = await browser.newPage();
    });

    afterAll(async () => {
        await browser.close();
    });

    test('should load the dashboard home page', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.waitForSelector('h1.h3.mb-0.text-gray-800');
        const title = await page.$eval('h1.h3.mb-0.text-gray-800', el => el.textContent);
        expect(title).toBe('Prescribing Dashboard');
    }, 30000);

    test('should display total items tile', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.waitForSelector('.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1');
        const totalItemsText = await page.$eval('.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1', el => el.textContent);
        expect(totalItemsText).toContain('Total items:');
    }, 30000);

    test('should display top prescribed item', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.waitForSelector('.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1');
        const topPrescribedItemText = await page.$eval('.text-xs.font-weight-bold.text-primary.text-uppercase.mb-1', el => el.textContent);
        expect(topPrescribedItemText).toContain('TOP PRESCRIBED ITEM:');
    }, 3000000);

    test('should submit form and update chart', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.waitForSelector('#input-group-select-2');
        await page.select('#input-group-select-2', '01C');
        await page.click('input[type="submit"]');
        await page.waitForSelector('#chart2');
        const chartExists = await page.$eval('#chart2', el => !!el);
        expect(chartExists).toBe(true);
    }, 300000000);

    test('should calculate BMI', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.click('div[onclick="popup.showBMICalcFormPopup();"]');
        await page.waitForSelector('#BMI-calc');
        await page.type('#weight1', '70');
        await page.type('#height1', '170');
        await page.click('#ctc-button');
        await page.waitForSelector('#BMIresult');
        const bmiResult = await page.$eval('#BMIresult', el => el.textContent);
        expect(bmiResult).toContain('The estimated BMI result is:');
    }, 300000000);

    test('should calculate creatinine clearance', async () => {
        await page.goto('http://localhost:5000/dashboard/home/');
        await page.click('div[onclick="popup.showCeatCalcFormPopup();"]');
        await page.waitForSelector('#creat-calc');
        await page.type('#age', '30');
        await page.type('#weight', '70');
        await page.type('#serum-creatinine', '100');
        await page.select('#sex', 'Male');
        await page.click('#ctc-button');
        await page.waitForSelector('#result');
        const creatinineResult = await page.$eval('#result', el => el.textContent);
        expect(creatinineResult).toContain('The estimated creatinine clearance result is:');
    }, 30000);
});