/**
* A basic Hello World function
* @param {string} name Who you're saying hello to
* @returns {string}
*/
const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});
//const lib = require('lib')({token: "tok_dev_W5mbaAJHdKbCkHVaejgt6kEmUSSR6x9rwAZRoaEYrtLQVm8rns8Kr5mBC92Trduq"});
/**
* An HTTP endpoint that acts as a webhook for HTTP or Webhook request event
* @returns {object} result The result of your workflow steps
*/
module.exports = async (email = '', subject = '', text = '',context) => {

  // Prepare workflow object to store API responses

  let result = {};

  // [Workflow Step 1]

  console.log(`Running gmail.messages[@0.1.6].create()...`);

  result.step1 = {};
  result.step1.message = await lib.gmail.messages['@0.1.6'].create({
    to: email, // required
    subject: subject,
    cc: null,
    bcc: null,
    text: text,
    html: null
  });

  return result;
};