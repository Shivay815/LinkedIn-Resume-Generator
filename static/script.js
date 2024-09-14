document.getElementById('resumeForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent form from submitting the traditional way

    console.log('Form submission triggered');  // Log form submission

    // Grab the values from the form
    const openAiKey = document.getElementById('open_ai_key').value;
    const pdfFile = document.getElementById('pdf_file').files[0];

    console.log('OpenAI Key:', openAiKey);  // Log OpenAI Key
    console.log('PDF File:', pdfFile ? pdfFile.name : 'No file selected');  // Log the PDF file name

    // Ensure both fields are filled out
    if (!openAiKey || !pdfFile) {
        alert("Please provide an OpenAI key and a LinkedIn PDF file.");
        console.log('Form validation failed: missing OpenAI key or PDF file');  // Log form validation failure
        return;
    }

    // Create FormData object to send via the API
    const formData = new FormData();
    formData.append('open_ai_key', openAiKey);
    formData.append('pdf_file', pdfFile);

    console.log('FormData created:', formData);  // Log FormData creation

    // Call the Flask API using Fetch API
    try {
        console.log('Sending request to /api/generate_resume...');  // Log API request start

        const response = await fetch('http://127.0.0.1:5000/api/generate_resume', {
            method: 'POST',
            body: formData
        });

        console.log('API response received:', response);  // Log the raw response

        // Parse JSON response
        const result = await response.json();
        console.log('Parsed response:', result);  // Log parsed JSON response

        if (response.ok && result.generated_resume) {
            console.log('Resume generated successfully');  // Log success

            // If success, redirect to another HTML page and display the generated resume
            localStorage.setItem('generated_resume', result.generated_resume); // Store the resume in local storage
            console.log('Resume saved to localStorage');  // Log storage success

            window.location.href = 'resume.html';  // Redirect to the resume display page
        } else {
            alert(result.message || 'Error generating resume. Please try again.');
            console.log('API error or missing resume:', result.message);  // Log error message
        }
    } catch (error) {
        console.error('Error:', error);  // Log API call failure
        alert('Failed to call API. Please try again later.');
    }
});
