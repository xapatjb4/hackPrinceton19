const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
/**
* An HTTP endpoint that acts as a webhook for HTTP or Webhook request event
* @returns {object} result The result of your workflow steps
*/
module.exports = async (name = "world", email = "5089816164@txt.att.net",context) => {

  // Prepare workflow object to store API responses

  let result = {};

  // [Workflow Step 1]

  console.log(`Running gmail.messages[@0.1.6].create()...`);

  result.step1 = {};
  result.step1.message = await lib.gmail.messages['@0.1.6'].create({
    to: email,
    subject: `Battery at 50%`,
    cc: null,
    bcc: null,
    text: "Hi "+ name + ", this is to inform you that your glass batteries are at 50%",
    html: null
  });

  return result;
};