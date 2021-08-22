// MIT License
//
// Copyright(c) 2021 Mark Whitney
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>


const cv::Scalar SCA_BLACK = cv::Scalar(0, 0, 0);
const cv::Scalar SCA_WHITE = cv::Scalar(255, 255, 255);
const cv::Scalar SCA_GRAY = cv::Scalar(128, 128, 128);
const cv::Scalar SCA_MAGENTA = cv::Scalar(255, 0, 255);


typedef struct
{
    char tag;
    int row;
    int col;
    int num;
    int seq;
} T_PUZZ_STEP;

typedef std::vector<std::string> tVecStr;
typedef std::vector<T_PUZZ_STEP> tVecPuzzStep;


static int _puzznum[9][9];
static char _puzztag[9][9];
static tVecPuzzStep _vzz;


void read_file(const std::string& rs, tVecStr& rvec)
{
    std::ifstream ifs;
    ifs.open(rs);
    if (ifs.is_open())
    {
        std::string ss;
        while (std::getline(ifs, ss))
        {
            rvec.push_back(ss);
        }
        ifs.close();
    }
}

void parse_solution(tVecStr& rvec)
{
    size_t ii = 0;
    size_t jj = 0;

    for (const auto& rs : rvec)
    {
        tVecStr vtok;
        std::string stok;
        std::istringstream iss(rs);
        while (std::getline(iss, stok, ','))
        {
            vtok.push_back(stok);
        }

        if ((vtok.size() == 9) && (jj < 9))
        {
            // first nine lines are the 9x9 puzzle
            for (ii = 0; ii < 9; ii++)
            {
                _puzznum[jj][ii] = atoi(vtok[ii].c_str());
                _puzztag[jj][ii] = '\0';
            }
            jj++;
        }
        else if (vtok.size() == 5)
        {
            // remaining lines are steps of solution
            // (last 9 lines are final solution but are ignored)
            T_PUZZ_STEP zz;
            zz.tag = vtok[0][0];
            zz.row = atoi(vtok[1].c_str());
            zz.col = atoi(vtok[2].c_str());
            zz.num = atoi(vtok[3].c_str());
            zz.seq = atoi(vtok[4].c_str());
            _vzz.push_back(zz);
        }
    }
}


void render_puzzle_text(tVecStr& rv)
{
    const std::string hborder = "----------------------------------";
    size_t ii;
    size_t jj;

    rv.clear();

    for (jj = 0; jj < 9; jj++)
    {
        if ((jj % 3) == 0)
        {
            rv.push_back(hborder);
        }

        std::ostringstream oss;
        for (ii = 0; ii < 9; ii++)
        {
            if ((ii % 3) == 0)
            {
                oss << "| ";
            }
            oss << _puzznum[jj][ii] << " ";
        }
        oss << "|";
        rv.push_back(oss.str());
    }

    rv.push_back(hborder);
}


void render_puzzle_step(cv::Mat& rimg, const T_PUZZ_STEP& rz)
{
    int ii;
    int jj;
    int k1 = 80;
    int k3 = k1 * 3;
    int k9 = k1 * 9;
    int kii = 23;
    int kjj = 53;
    double fscale = 3.0;

    if (rz.tag != '\0')
    {
        // update global puzzle
        _puzznum[rz.row][rz.col] = rz.num;
        _puzztag[rz.row][rz.col] = rz.tag;
    }

    rimg = cv::Mat::zeros({ k9, k9 }, CV_8UC3);

    // fill with white
    // and draw border around whole thing
    cv::rectangle(rimg, { 0,0,k9,k9 }, SCA_WHITE, -1);
    cv::rectangle(rimg, { 0,0,k9,k9 }, SCA_BLACK, 7);

    // draw 3 x 3 borders
    for (jj = 0; jj < 3; jj++)
    {
        for (ii = 0; ii < 3; ii++)
        {
            cv::rectangle(rimg, { ii * k3, jj * k3, k3, k3 }, { 0,0,0 }, 3);
        }
    }

    // draw 9 x 9 borders and numbers
    for (jj = 0; jj < 9; jj++)
    {
        for (ii = 0; ii < 9; ii++)
        {
            int num = _puzznum[jj][ii];
            char tag = _puzztag[jj][ii];
            cv::rectangle(rimg, { ii * k1, jj * k1, k1, k1 }, SCA_BLACK, 1);
            if (num != 0)
            {
                cv::Scalar sca = SCA_BLACK;
                switch (tag)
                {
                    case 'G':
                    case 'N':
                        // guessed (or next guess) square
                        sca = SCA_MAGENTA;
                        break;
                    case 'U':
                        // solved square (unique)
                        sca = SCA_GRAY;
                        break;
                    default:
                        // original square
                        sca = SCA_BLACK;
                        break;
                }
                std::ostringstream oss;
                oss << num;
                putText(rimg, oss.str(),
                    { (ii * k1) + kii, (jj * k1) + kjj },
                    cv::FONT_HERSHEY_PLAIN, fscale, sca, 3);
            }
        }
    }
}



int main()
{
    std::cout << "Sudoku Solution Visualizer\n";

    cv::Mat img;
    tVecStr vpuzz;
    tVecStr vs;
    int nn = 0;
    int reps = 60;

    read_file("C:\\work\\ss\\ss_vs2019\\solution1.txt", vs);
    parse_solution(vs);

    for (int ii = 0; ii < reps; ii++)
    {
        // render initial puzzle
        std::ostringstream oss;
        oss << "foo" << std::setw(4) << std::setfill('0') << nn << ".png";
        render_puzzle_step(img, { 0 });
        cv::imwrite(oss.str(), img);
        nn++;
    }

    for (const auto& rz : _vzz)
    {
        // render all steps
        std::ostringstream oss;
        oss << "foo" << std::setw(4) << std::setfill('0') << nn << ".png";
        render_puzzle_step(img, rz);
        cv::imwrite(oss.str(), img);
        nn++;
    }

    // clear tags so all squares are black again
    memset(_puzztag, 0, sizeof(_puzztag));

    for (int ii = 0; ii < reps; ii++)
    {
        // render final solved puzzle
        std::ostringstream oss;
        oss << "foo" << std::setw(4) << std::setfill('0') << nn << ".png";
        render_puzzle_step(img, { 0 });
        cv::imwrite(oss.str(), img);
        nn++;
    }

    return 0;
}
