# Wine data analysis complete project
install.packages("rstudioapi")
library("rstudioapi")

# TODO: Find a way to generalize the location of winequality-red.csv
file_path <- getSourceEditorContext()$path

wine_data_path <- paste(substr(file_path, 0, nchar(file_path)-7), "winequality-red.csv", sep="")
print(wine_data_path)

# Load csv
wine_data_red <- read.csv(file=wine_data_path, header=TRUE, sep=';')
str(wine_data_red)

# summary
summary(wine_data_red)

# Mean and trimmed mean of all variables by removing 0.1 fraction of values on both ends
for (col in colnames(wine_data_red)) {
  cat(col, "\n")
  cat("Mean: ", mean(wine_data_red[[col]]), "\n")
  cat("Trimmend Mean: ", mean(wine_data_red[[col]], trim=0.1), "\n")
}

# No example for weighted mean and median?

# quantiles for fixed density
# standard deviation
sd(wine_data_red[['fixed.acidity']])
# Inter quantile range
IQR(wine_data_red[['fixed.acidity']])
# Median absolute deviation
mad(wine_data_red[['fixed.acidity']])


quantile(wine_data_red[['volatile.acidity']], p=c(0.05, 0.25, 0.5, 0.75, 0.95))
boxplot(wine_data_red[['volatile.acidity']])

