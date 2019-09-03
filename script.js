const imageUpload = document.getElementById('imageUpload')

Promise.all([
    faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
]).then(start)

function start() {
    //create a <div container /> and set its css position to 'relative'
    const container = document.createElement('div')
    container.style.position = 'relative'
    document.body.append(container)
    document.body.append('Loaded')

    imageUpload.addEventListener('change', async() => {
        //pass the uploaded image to a variable 'image'
        const image = await faceapi.bufferToImage(imageUpload.files[0])
        container.append(image)

        //create a canvas according to the upload image
        const canvas = faceapi.createCanvasFromMedia(image)
        container.append(canvas)

        //match the canvas size with the image size
        const displaySize = {width: image.width, height: image.height}
        faceapi.matchDimensions(canvas, displaySize)

        const detections = await faceapi.detectAllFaces(image)
        .withFaceLandmarks().withFaceDescriptors()
        const resizedDetections = faceapi.resizedResults(detections, displaySize)
        resizedDections.forEach(detection => {
            const box = detection.detection.box
            const drawBox = new faceapi.draw.DrawBox(box, { label: 'Face'})
            drawBox.draw(canvas)
        })
                
        
    })
}