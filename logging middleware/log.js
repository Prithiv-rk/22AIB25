require("dotenv").config();
const TEST_SERVER_URL = process.env.TEST_SERVER_URL;
const ACCESS_TOKEN = process.env.ACCESS_TOKEN;
async function log(stack,level,package,message ){
    const payload={
        stack,
        level,
        package:packageName,
        message
    }
};
try {
    const response = await fetch(TEST_SERVER_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ACCESS_TOKEN}`
        },
        body: JSON.stringify(payload)
    });
    if (!response.ok) {
        throw new Error(`Error logging message: ${response.statusText}`);
    }
} catch (error) {
    console.error("Logging error:", error);
}