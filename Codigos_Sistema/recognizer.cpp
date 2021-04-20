#include "opencv2/opencv.hpp"
#include "opencv2/core.hpp"
#include "opencv2/objdetect.hpp"
#include "opencv2/face.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"

#include <iostream>
#include <ctime>
#include <fstream>
#include <map>

using namespace cv;
using namespace cv::face;
using namespace std;


int main(int argc, char *argv[])
{
	VideoCapture cap(0); // WebCam

	map<int, string> labels;

	ifstream infile("./recognizer/labels.txt");

	int a;
	string b;
	while (infile >> a >> b){
		labels[a] = b;
	}

	if(!cap.isOpened()) {
		return -1;
	}

	CascadeClassifier classifier;
	classifier.load("./cascades/lbpcascade_frontalface.xml");

	Ptr<LBPHFaceRecognizer>recognizer =  LBPHFaceRecognizer::create(2, 2, 7, 7, 17);
	recognizer->read("./recognizer/embeddings.xml");

	Mat windowFrame;
	namedWindow("edges", 1);
	int numframes = 0;
	time_t timer_begin,timer_end;
	time ( &timer_begin );

	for(;;){
		Mat frame; // Matriz de Frames
		cap >> frame;

		cvtColor(frame, windowFrame, COLOR_BGR2GRAY); // converte para cinza
		
		vector<Rect> faces;
		
		classifier.detectMultiScale(frame, faces, 1.2, 5);
		
		for(size_t i = 0; i < faces.size(); i++){
			rectangle(frame, faces[i], Scalar(0, 255, 0));
			Mat face = windowFrame(faces[i]);
			double confidence = 0.0;
			int predicted = recognizer->predict(face);
			recognizer->predict(face, predicted, confidence);
			if(labels.find(predicted) == labels.end() || confidence < 25){
				putText(frame, "Unknown", Point(faces[i].x ,faces[i].y - 5), FONT_HERSHEY_DUPLEX, 1, Scalar(0,255,0), 1);
			}else{
				putText(frame, labels[predicted], Point(faces[i].x ,faces[i].y - 5), FONT_HERSHEY_DUPLEX, 1, Scalar(0,255,0), 1);
			}
			cout << "ID: " << predicted << " | Confidence: " << confidence << endl;
		}
		
		imshow("edges", frame);
		numframes++;

		if(waitKey(30) >=0) break;
	}
	
	return 0;
}
